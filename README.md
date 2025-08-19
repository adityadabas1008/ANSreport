# ANSreport

Hello there! Welcome to the ANSreport repository.

This repository is a combined work of the students of the course "Analoge Schaltungen" from the Hochschule Bremen, under the mentorship of Prof. Dr. Mirco Meiners.

The contributors are:
- Aditya Dabas
- Adrian Jauch
- Mohamad Wehbi

What you see here is a quarto report of a project from the 'Texas Instruments Analog Circuits Lab Kit' manual.

The project aimed at building deeper understanding of analog circuits using the universal biquad filter design.
Here, we implemented the second order biquad filter in three different stages:
1. **The theory level**: Here, we explored the ideal world of Electronics by simulating the circuit in KiCAD.
2. **Filter on a discrete circuit design**: After that the circuit was build on the lab board of ASLK using jumper wires, was somewhat imperfect, but still worked.
3. **The integrated PCB Design**: Then we wanted to explore the PCB design of the circuit, so we designed the biquad filter on a PCB, in a compact form and checked the functionality in the lab, we also tried to expand the circuit by adding another order to our second order filter, by cascading a second order filter to another butterworth filter to get a third order filter and a cleaner curve.

Now, its upto you to explore the interesting results we got in the ideal world and the real world of electronics.
Another question would be, were we able to successfully cascade the second order filter to a third order filter to get the butterworth output ? was it successful on the compact PCB we designed ?

Run the report to find out!

## How to run the report
1. Clone the repository as it is.
2. Choose the editor of your choice, e.g. [VSCode](https://code.visualstudio.com/).
3. Make sure you have [quarto](https://quarto.org/docs/get-started/) installed.
4. Just render the index.qmd file in the editor.
Voila! You should see the report in your browser.

Thank you for your interest in our project!