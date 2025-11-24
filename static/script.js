async function send(){
    let q = document.getElementById("question").value
    let mode = document.getElementById("mode").value
    let chat = document.getElementById("chat")

    chat.innerHTML += "<div><b>Bạn:</b> " + q + "</div>"

    let res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question:q, style:mode})
    })

    let data = await res.json()
    let text = data.choices?.[0]?.message?.content || "Lỗi API"

    chat.innerHTML += "<div><b>Bot:</b> " + text + "</div>"
}
