    post_edit_form.addEventListener("submit", (e) =>{
        e.preventDefault()

        const data = new FormData(post_edit_form);
        const json_data = Object.fromEntries(data)
        console.log(json_data)
        console.log(json_data["title"])

        document.querySelector(`#p_title${json_data.post}`).innerHTML = json_data.title
        document.querySelector(`#p_author${json_data.post}`).innerHTML = json_data.author


    })