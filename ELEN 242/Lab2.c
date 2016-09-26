#include <board.h>
#include <sysclk.h>
#include <stdio.h>
#include <stdio_serial.h>

// GPIO Registers
#define PORTA_PIO_PDR		*(volatile int *) 0x400E0E04
#define PORTA_PIO_ABCDSR1	*(volatile int *) 0x400E0E70
#define PORTA_PIO_ABCDSR2	*(volatile int *) 0x400E0E74

#define PORTB_PIO_PER		*(volatile int *) 0x400E1000
#define PORTB_PIO_PDR		*(volatile int *) 0x400E1004
#define PORTB_PIO_OER		*(volatile int *) 0x400E1010
#define PORTB_PIO_ODR		*(volatile int *) 0x400E1014
#define PORTB_PIO_SODR		*(volatile int *) 0x400E1030
#define PORTB_PIO_CODR		*(volatile int *) 0x400E1034
#define PORTB_PIO_ODSR		*(volatile int *) 0x400E1038
#define PORTB_PIO_PDSR		*(volatile int *) 0x400E103C
#define PORTB_PIO_ABCDSR1	*(volatile int *) 0x400E1070
#define PORTB_PIO_ABCDSR2	*(volatile int *) 0x400E1074

#define PORTC_PIO_PER		*(volatile int *) 0x400E1200
#define PORTC_PIO_PDR		*(volatile int *) 0x400E1204
#define PORTC_PIO_OER		*(volatile int *) 0x400E1210
#define PORTC_PIO_ODR		*(volatile int *) 0x400E1214
#define PORTC_PIO_SODR		*(volatile int *) 0x400E1230
#define PORTC_PIO_CODR		*(volatile int *) 0x400E1234
#define PORTC_PIO_ODSR		*(volatile int *) 0x400E1238
#define PORTC_PIO_PDSR		*(volatile int *) 0x400E123C
#define PORTC_PIO_IER		*(volatile int *) 0x400E1240
#define PORTC_PIO_ISR		*(volatile int *) 0x400E124C
#define PORTC_PIO_AIMER		*(volatile int *) 0x400E12B0
#define PORTC_PIO_REHLSR	*(volatile int *) 0x400E12D4

// UART 0 Registers
#define UART0_CR			*(volatile int *) 0x400E0600
#define UART0_MR			*(volatile int *) 0x400E0604
#define UART0_SR			*(volatile int *) 0x400E0614
#define UART0_RHR			*(volatile int *) 0x400E0618
#define UART0_THR			*(volatile int *) 0x400E061C
#define UART0_BRGR			*(volatile int *) 0x400E0620

// UART Control Register bits
#define UART_CR_TXDIS		0x80
#define UART_CR_TXEN		0x40
#define UART_CR_RXDIS		0x20
#define UART_CR_RXEN		0x10
#define UART_CR_RSTTX		0x08
#define UART_CR_RSTRX		0x04

// UART Mode Register bits
#define UART_MR_NOPARITY	0x800

// UART Status Register bits
#define UART_SR_TXRDY		0x02
#define UART_SR_RXRDY		0x01

// SPI Registers
#define SPI_CR				*(volatile int *) 0x40008000
#define SPI_MR				*(volatile int *) 0x40008004
#define SPI_RDR				*(volatile int *) 0x40008008
#define SPI_TDR				*(volatile int *) 0x4000800C
#define SPI_SR				*(volatile int *) 0x40008010
#define SPI_CSR0			*(volatile int *) 0x40008030

// SPI Control Register bits
#define SPI_CR_SPIEN		0x01

// SPI Mode Register bits
#define SPI_MR_MSTR			0x01

// SPI Status Register bits
#define SPI_SR_TDRE			0x02
#define SPI_SR_RDRF			0x01

// ADC Registers
#define ADC_CR				*(volatile int *) 0x40038000
#define ADC_MR				*(volatile int *) 0x40038004
#define ADC_CHER			*(volatile int *) 0x40038010
#define ADC_CHDR			*(volatile int *) 0x40038014
#define ADC_CHSR			*(volatile int *) 0x40038018
#define ADC_CDR0			*(volatile int *) 0x40038050
#define ADC_ACR				*(volatile int *) 0x40038094

// ADC Control Register Bits
#define ADC_START			0x02
#define ADC_SWRST			0x01

// ADC Mode Register Bits
#define ADC_TRANSFER		0x30000000
#define ADC_PRESCAL			PRESCAL_VALUE * 0x100
#define ADC_LOWRES			0x10
#define PRESCAL_VALUE		0x00			// <---- Change this value to change prescaler

// ADC Channel Enable Register Bits
#define ADC_EN_CH0			0x01

// ADC Channel Disable Register Bits
#define ADC_DIS_CH0			0x01

// ADC Channel Status Register Bits
#define ADC_STAT_CH0		0x01

// ADC Analog Control Register Bits
#define ADC_IRCE			0x04
#define ADC_FORCEREF		0x80000

// Timer 0 channel 0 registers
#define TC_CCR0_CH0			*(volatile int *) 0x40010000
#define TC_CMR0_CH0			*(volatile int *) 0x40010004
#define TC_CVR0_CH0			*(volatile int *) 0x40010010
#define TC_RA0_CH0			*(volatile int *) 0x40010014
#define TC_RB0_CH0			*(volatile int *) 0x40010018
#define TC_RC0_CH0			*(volatile int *) 0x4001001C
#define TC_SR0_CH0			*(volatile int *) 0x40010020
#define TC_IER0_CH0			*(volatile int *) 0x40010024
#define TC_IDR0_CH0			*(volatile int *) 0x40010028
#define TC_IMR0_CH0			*(volatile int *) 0x4001002C

// Timer 0 Channel 0 Channel Control Register Bits
#define CCR_SWTRG			0x04
#define CCR_CLKDIS			0x02
#define CCR_CLKEN			0x01

// Timer 0 Channel 0 Channel Mode Register Bits
#define CMR_WAVE_EN			0x8000
#define CMR_WAVE_SEL		0x4000
#define CMR_DIV_32			0x02

// Timer 0 Channel 0 Status Register Bits
#define SR_CPCS				0x10

// Timer 0 Channel 0 Interrupt Enable/Disable/Mask Register Bits
#define INT_CPCS			0x10

// PWM Module 0
#define PWM_MR				*(volatile int *) 0x40020000
#define PWM_ENA				*(volatile int *) 0x40020004
#define PWM_DIS				*(volatile int *) 0x40020008
#define PWM_SR				*(volatile int *) 0x4002000C
#define PWM_CMR0			*(volatile int *) 0x40020200
#define PWM_CDTY0			*(volatile int *) 0x40020204
#define PWM_CPRD0			*(volatile int *) 0x40020208
#define PWM_CCNT0			*(volatile int *) 0x4002020C
#define PWM_CUPD0			*(volatile int *) 0x40020210

#define CHID0				0x01

// Function prototypes
void gpio_init();
void uart0_init();
void delay_ms(unsigned short delay_time);
void delay_us(unsigned short delay_time);
unsigned char GetCharacter();
void PutCharacter(unsigned char ch);



int main(void)
{

	// Initialize the clock
	sysclk_init();

	// Initialize the GPIO modules
	gpio_init();
	
	// Initialize UART0 to 9600, 8, N, 1
	uart0_init();

	// Infinite loop
	while (true)
	{

		PutCharacter('B');
		PutCharacter('e');
		PutCharacter('e');
		PutCharacter('p');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(27);
		PutCharacter('[');
		PutCharacter('1');
		PutCharacter(';');
		PutCharacter('0');
		PutCharacter('H');
		PutCharacter('B');
		PutCharacter('o');
		PutCharacter('o');
		PutCharacter('p');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		
		delay_ms(5000);
		
		PutCharacter(27);
		PutCharacter('[');
		PutCharacter('0');
		PutCharacter(';');
		PutCharacter('0');
		PutCharacter('H');
		
		PutCharacter('P');
		PutCharacter('r');
		PutCharacter('i');
		PutCharacter('n');
		PutCharacter('t');
		PutCharacter('i');
		PutCharacter('n');
		PutCharacter('g');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		
		delay_ms(5000);
		
		PutCharacter(27);
		PutCharacter('[');
		PutCharacter('1');
		PutCharacter(';');
		PutCharacter('0');
		PutCharacter('H');
		
		PutCharacter('T');
		PutCharacter('e');
		PutCharacter('x');
		PutCharacter('t');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');
		PutCharacter(' ');

	}
}


// User subroutines go here



void uart0_init() {
	
	// Send a clock signal to this UART module
	pmc_enable_periph_clk(ID_UART0);
	// Set the baud rate to 9600 as per the formula provided.
	UART0_BRGR = ((120000000/9600)/16);
	// Set the mode to no parity.
	UART0_MR = UART_MR_NOPARITY;
	// Enable the UART1 receiver and transmitter.
	UART0_CR = UART_CR_RXEN | UART_CR_TXEN;
}

void gpio_init() {

	// Initialize GPIO modules by sending a clock signal to each I/O port
	pmc_enable_periph_clk(ID_PIOA);
	pmc_enable_periph_clk(ID_PIOB);
	pmc_enable_periph_clk(ID_PIOC);
	
	// We want to configure Port C, bits 24-27 as inputs
	// 0000 1111 0000 0000 0000 0000 0000 0000
	//     0F        00        00        00
	// We want to configure Port C, bits 19-22 as outputs
	// 0000 0000 0111 1000 0000 0000 0000 0000
	//     00        78        00        00
	
	// So enable all 8 of these bits in the Port C Pin Enable Register
	PORTC_PIO_PER = 0x0F780000;
	// Configure bits 19-22 as outputs in the Port C Output Enable Register
	PORTC_PIO_OER = 0x00780000;
	// Configure bits 24-27 as inputs in the Port C Output Disable Register
	PORTC_PIO_ODR = 0x0F000000;

	// We want to configure Port A, bits 9-10 for Peripheral A functionality (UART0)
	// 0000 0000 0000 0000 0000 0110 0000 0000
	//     00        00        06        00
	
	// So disable these 2 bits in the Port A Pin Disable Register
	PORTA_PIO_PDR = 0x00000600;
	// And assign them to Peripheral A functionality by writing 00 to both of
	// the Port A Peripheral Select Registers
	PORTA_PIO_ABCDSR1 = 0x00;
	PORTA_PIO_ABCDSR2 = 0x00;
}

void delay_ms(unsigned short delay_time) {
	// Declare variables
	unsigned short i;
	
	// outer loop
	while (1) {
		// inner for loop
		// Wait 1 millisecond
		for (i=0; i<9206; i++) {
			// do nothing
		}
		// decrement delay_time
		delay_time--;
		// see if it is time to leave
		if (delay_time == 0) {
			// break out of this infinite loop
			break;
		}
	}
}

void delay_us(unsigned short delay_time) {
	// Declare variables
	unsigned char i;
	
	// outer loop
	while (1) {
		// inner for loop
		// Wait 1 millisecond
		for (i=0; i<9; i++) {
			// do nothing
		}
		// decrement delay_time
		delay_time--;
		// see if it is time to leave
		if (delay_time == 0) {
			// break out of this infinite loop
			break;
		}
	}
}

void PutCharacter(unsigned char ch)
{
	while(!(UART0_SR & UART_SR_TXRDY))
	{
		;
	}
	UART0_THR = ch;
}

unsigned char GetCharacter()
{
	while(!(UART0_SR & UART_SR_RXRDY))
	{
		;
	}
	return (UART0_RHR);
}