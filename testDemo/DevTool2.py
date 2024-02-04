# const data = {
#   firstname: 'Ana',
#   lastname: 'Pooh',
#   gender: 'Female',
#   yearsOfExpirience: 7,
#   profession: ['Automation Tester', 'Manual Tester'],
#   tools: ['Selenium Webdriver', 'Selenium IDE'],
#   continent: 'Antartica'
# };
#
# // Fill text fields
# document.getElementById('firstname').value = data.firstname;
# document.getElementById('lastname').value = data.lastname;
#
# // Select radio button
# const genderRadio = document.querySelector(`input[value="${data.gender}"]`);
# if (genderRadio) {
#   genderRadio.checked = true;
# }
#
# // Select years of experience
# const experienceSelect = document.getElementById('selenium-experience');
# for (let i = 0; i < experienceSelect.options.length; i++) {
#   if (experienceSelect.options[i].value === data.yearsOfExpirience.toString()) {
#     experienceSelect.options[i].selected = true;
#     break;
#   }
# }
#
# // Select profession checkboxes
# const professionChecks = document.querySelectorAll('[name="profession"]');
# for (const check of professionChecks) {
#   if (data.profession.includes(check.value)) {
#     check.checked = true;
#   }
# }
#
# // Select automation tools checkboxes
# const toolsChecks = document.querySelectorAll('[name="tool"]');
# for (const check of toolsChecks) {
#   if (data.tools.includes(check.value)) {
#     check.checked = true;
#   }
# }
#
# // Select continent
# const continentSelect = document.getElementById('continents');
# for (let i = 0; i < continentSelect.options.length; i++) {
#   if (continentSelect.options[i].text === data.continent) {
#     continentSelect.options[i].selected = true;
#     break;
#   }
# }
#
# // Click submit button
# document.getElementById('submit-button').click();
