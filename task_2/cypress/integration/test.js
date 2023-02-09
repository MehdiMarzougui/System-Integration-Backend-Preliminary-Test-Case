///<reference types="cypress"/>

context("test_req", () => {
    // Visiting the tested website is executed before each test
    beforeEach(() => {
        cy.visit("https://butopea.com/")
    })

    it('test_1: check if square has a text and button', () => {
        //select the container (sqaure) to be tested
        cy.get(".banner-square-overlay-container").within(() => {
            //assert statement to check the existence of elements
            cy.get('p').should('exist')
            cy.get('button').should('exist')

            const elements = ['p', 'button'];
            //check that both elments exist
            cy.get(elements.join(', ')).its('length')
                .then((length) => {
                    if (length === elements.length) {
                        // all elements exist, iterate through the elements and log their content
                        cy.log(`both the text and button exist within the square`);
                        elements.forEach((element) => {
                            cy.get(element).then((el) => {
                                cy.log(`Text of the ${element} is: ${el.text()}`);
                            });
                        });
                    } else {
                        //fail test
                        cy.fail('Not all elements exist');
                    }
                });

        })
    })

    it('test_2: check if square has an image', () => {
        //select the container to be testes
        cy.get(".banner-square-wrapper").within(() => {
            //test the existance of the image
            cy.get("img").eq(1).then(($img) => {
                if ($img.length > 0) {
                    //assert and extract the Image url
                    cy.get("img").should("exist")
                    cy.log("https://butopea.com/" + $img.attr("src"))
                } else {
                    //fail test otherwise
                    cy.fail('sqaure does not contain image');
                }
            })
        })

    })

    it('test_3:extract the productss details from the new product tab', () => {
        // Navigate to the target page and wait 2s second for it to load
        cy.get(':nth-child(3) > .secondary-font').click()
        cy.wait(2000)
        //Select the product list container
        cy.get('.product-listing').then((el) => {
            //make sure container is not empty
            if (el.length > 0) {
                //iterate over the container an extract product details
                cy.get('.product-listing > *').each((el, index) => {
                    cy.log(`Child ${index}:`)
                    cy.log('title: ' + el.find('p').text())
                    cy.log('price: ' + el.find('.product > [data-testid=productLink] > .product-tile-info > .lh30').text())
                    cy.log("Link: https://butopea.com" + el.find('a').attr("href"))
                    cy.log("image link: https://butopea.com" + el.find("img").eq(1).attr('src'))
                })

            } else {
                //fail test
                cy.fail('there is no list of products');
            }
        })


    })

})

