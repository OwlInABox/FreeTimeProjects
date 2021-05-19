/*
 * interruptHandler.c
 *
 * Created: 21/02/2020 10:19:19
 *  Author: nico835t
 */ 


#include <avr/io.h>
#include <avr/interrupt.h>

ISR(TIMER1_COMPA_vect)
{
  PORTB &= ~(0x21);
  TCCR1B &= ~(0x05);
}

ISR(INT0_vect)
{
	// when activated turn on LED
	PORTB |= 0x21; // toggles PB0 and PB5 between output low and output high
	TCCR1B |= 0x05; // sets prescale and starts timer
	
	
	 
	
}
