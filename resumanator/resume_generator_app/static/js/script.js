
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOMContentLoaded event fired");
    
    const form = document.getElementById('resumeForm');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const addSkillButton = document.getElementById("addSkill");
    const skillsList = document.getElementById("skillsList");

    addSkillButton.addEventListener("click", function () {
        console.log("Add Skill button clicked");

        const skillItem = document.createElement("li");
        skillItem.innerHTML = '<input type="text" name="skills[]" required>';
        skillsList.appendChild(skillItem);
    });

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        formData.append('csrfmiddlewaretoken', csrfToken);

        try {
            const response = await fetch(generateResumeUrl, {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                if (data.success) {
                    const generatedResume = data.generated_resume;
                    // Display the generated resume in your frontend
                    document.getElementById('resumeOutput').innerHTML = generatedResume;
                } else {
                    console.error('Failed to generate resume:', data.message);
                }
            } else {
                console.error('Failed to fetch:', response.status);
            }
        } catch (error) {
            console.error('An error occurred:', error);
        }
    });
});
