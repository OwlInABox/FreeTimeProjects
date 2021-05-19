/*
 * setup.c
 *
 * Created: 21/02/2020 10:13:32
 *  Author: nico835t
 */ 
#include <avr/io.h>
#include <avr/interrupt.h>


void interruptSetup(void)
{
	cli(); // clear interrupts
	EICRA = 0x03; // PD2. external interrupt. sents a interrupt signal when a button is pressed
	EIMSK = 0x01; // PD2. enables interrupt 0
	OCR1A = 0x3D08; // waits for 2 sec. clk=8Mhz prescale=1024 
	TCCR1B = 0x08; // set timer1 CTC mode 4
	TIMSK1 = 0x02;  // clockmask mode 4
	
  
	sei(); // enables global interrupts
	
	
	
	
}

void registerSetup(void)
{
	PORTB = 0x00;// set PB pins to be output low(sink)
	DDRB = 0x21; // PB0 and  PB5 are set to output
	
	DDRD = 0x00; // set PD0-PD7 to input
	PORTD = 0x04; // set PD2 to input with pull-up
	PIND = 0x04; // inverts  PD2
	
}

