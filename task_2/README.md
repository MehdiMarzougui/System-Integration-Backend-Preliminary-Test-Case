Task_2 

    instructions:
        - Using a terminal naavigate to ./cypress/integration
        - Type in the terminal the command npx cypress open (cypress v6.5)
        - the Cypress GUI will appear, choose the test.js and run it
        - The Test website will appear and on the left of the window you can expand the 3 different tests to monitor the logs
    explanation:
        - All tests start by visiting the website which is accomplished before the start of each test using the method beforeEach()
        - test1: Selected the container by its ID using the get() method and the searched for the required elements in th scope of the container, asserted the existence of the two elements (for logging) and then if both elements exist we log their contents.
        - test2: Selected the relevant the container and verified the exitence of an image object then logged src URL
        - test3: Started by selecting the tab and clicing using the get().click chain, then waited for 2 second for the page to load using wait(), I then selected the product container and  navigated to the relevant elements and logged their content or attributes
        

