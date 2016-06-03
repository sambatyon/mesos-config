# mesos-config
A launch script generator for Mesos

Interactive UI for generating configurations for Mesos Master and Agent


columns description:
label: variable name
name: human name
Description: hover over fuller description
type: check box, drop down list, radio button, text, text box
default value: I'm thinking of making this dynamic - in future fill out mini form to get sizing
required: booleen
validator: future use - validate valid values for free form entries

Some good features to have:
+ make generator profile based.
+ user can save configuration templates

http://mesos-config.techtamer.net
	The website uses the opensource "Form Tools"
	The export of the form is in csv, which will feed python which generates the bash script

