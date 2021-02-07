require('dotenv').config()

const express = require('express')
const app = express()
const jwt = require('jsonwebtoken')

app.use(express.json())

app.get('/posts', authenticateToken, (req, res) => {
    res.json({
        username: req.user.name,
        status: req.user.state
    })
})

app.post('/login', (req, res) => {
    const username = req.body.username
    const status = req.body.status

    const user = { name: username, state:status}


    const accessToken = jwt.sign(user, process.env.ACCESS_TOKEN_SECRET, { expiresIn: '60s' })
    res.json({ accessToken: accessToken })
})


function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization']
    const token = authHeader && authHeader.split(' ')[1]
    if (token == null) return res.sendStatus(401)

    jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
        console.log(err)
        if (err) return res.sendStatus(403)
        req.user = user
        next()
    })
}

app.listen(3000)
