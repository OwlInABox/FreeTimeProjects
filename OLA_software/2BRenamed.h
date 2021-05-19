/*

need to be renamed

*/ 
 
 void InterruptSetup(void)
{
	cli(); // clear interrupts
	EICRA = 0x03; // PD2. external interrupt. sents a interrupt signal when a button is pressed 
	EIMSK = 0x01; // PD2. enables interrupt 0
	sei(); // enables global interrupts
	
	
	
	
}

void registerSetup(void)
{
	PORTB = 0x00;// set PB to be output low(sink)
	DDRB = 0x21; // PB0 and  PB5 are set to output
	
	DDRD = 0x00; // set PD0-PD7 to input
	PORTD = 0x04; // set PD2 to input with pull-up
	PIND = 0x04; // inverts  PD2
	  
}

