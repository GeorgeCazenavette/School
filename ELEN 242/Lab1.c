#include <board.h>
#include <sysclk.h>

// Define statements
#define PORTC_PIO_PER	*(volatile int *) 0x400E1200
#define PORTC_PIO_OER	*(volatile int *) 0x400E1210
#define PORTC_PIO_ODR	*(volatile int *) 0x400E1214
#define PORTC_PIO_SODR	*(volatile int *) 0x400E1230
#define PORTC_PIO_CODR	*(volatile int *) 0x400E1234
#define PORTC_PIO_ODSR	*(volatile int *) 0x400E1238
#define PORTC_PIO_PDSR	*(volatile int *) 0x400E123C

int main(void)
{
	// Declare local variables
	unsigned int switches;
	unsigned int switch1, switch2, switch3, switch4;

	// Initialize the main board clock to 120 MHz.
	sysclk_init();

	// Initialize clock signals to the GPIO modules.
	pmc_enable_periph_clk(ID_PIOA);
	pmc_enable_periph_clk(ID_PIOB);
	pmc_enable_periph_clk(ID_PIOC);

	// We want to configure Port C, bits 19-22 as outputs
	// 0000 0000 0111 1000 0000 0000 0000 0000
	//     00        78        00        00

	// We want to configure Port C, bits 24-27 as inputs
	// 0000 1111 0000 0000 0000 0000 0000 0000
	//     0F        00        00        00
	
	// So enable all 8 of these bits in the Port C Pin Enable Register
	PORTC_PIO_PER = 0x0F780000;
	// Configure bits 19-22 as outputs in the Port C Output Enable Register
	PORTC_PIO_OER = 0x00780000;
	// Configure bits 24-27 as inputs in the Port C Output Disable Register
	PORTC_PIO_ODR = 0x0F000000;
	
	// Infinite loop
	while (1)
	{
		// Read from the switches connected to the Port C inputs
		switches = PORTC_PIO_PDSR;
		// Mask out the bits we don't want and keep the 4 bits we do want
		switches = switches & 0x0F000000;
		switch1 = (switches & 0x01000000) >> 5;
		switch2 = (switches & 0x02000000) >> 5;
		switch3 = (switches & 0x04000000) >> 5;
		switch4 = (switches & 0x08000000) >> 5;
		
		// Shift the input bits 5 bits to the right to match the output bits
		//switches = switches/32;
		
		// Set the bits in the Port C SODR to turn on the LEDs for the switches that are on
		//PORTC_PIO_SODR = switches;
		PORTC_PIO_SODR = ((switch1 << 2) | (switch2 >> 1) | (switch3 << 1) | (switch4 >> 2));
		// Set the bits in the Port C CODR to turn off the LEDs for the switches that are off
		//PORTC_PIO_CODR = ~switches;
		PORTC_PIO_CODR = ~((switch1 << 2) | (switch2 >> 1) | (switch3 << 1) | (switch4 >> 2));
	}

}
