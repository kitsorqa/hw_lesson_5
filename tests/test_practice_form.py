from selene import browser, command, have, be


def test_filling_and_sending_form():
    browser.open("/automation-practice-form")

    browser.element("#firstName").type("Test").press_enter()
    browser.element("#lastName").type("Sidorov").press_enter()
    browser.element("#userEmail").type("test@test.test").press_enter()
    browser.element('#gender-radio-1').perform(command.js.click())
    browser.element('#userNumber').type("8800553535")

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="8"]').click()
    browser.element('.react-datepicker__year-select').click().element("option[value='2002']").click()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#currentAddress').type("Улица Пушкина, дом Котолушкина").press_enter()
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()

    browser.element(".table").should(have.text("Test Sidorov"))
    browser.element(".table").should(have.text("test@test.test"))
    browser.element(".table").should(have.text("Male"))
    browser.element('.table').should(have.text('8800553535'))
    browser.element('.table').should(have.text('15 September,2002'))
    browser.element('.table').should(have.text('Computer Science'))
    browser.element('.table').should(have.text('Sports, Reading'))
    browser.element('.table').should(have.text('Улица Пушкина, дом Котолушкина'))
    browser.element('.table').should(have.text('Haryana Panipat'))
    browser.element('#closeLargeModal').should(be.clickable)