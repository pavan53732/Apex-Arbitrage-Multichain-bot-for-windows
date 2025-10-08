def notifySlack(String message, String channel = '#ci-alerts') {
    slackSend(channel: channel, message: message)
}

def notifyDiscord(String message, String webhookUrl) {
    sh "curl -X POST -H 'Content-Type: application/json' -d '{\"content\":\"${message}\"}' ${webhookUrl}"
}

def notifyTelegram(String message, String botToken, String chatId) {
    sh "curl -X POST https://api.telegram.org/bot${botToken}/sendMessage -d chat_id=${chatId} -d text='${message}'"
}

return this
