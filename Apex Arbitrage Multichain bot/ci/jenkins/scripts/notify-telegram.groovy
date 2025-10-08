def call(String message, String botToken, String chatId) {
    sh """
        curl -X POST https://api.telegram.org/bot${botToken}/sendMessage \
        -d chat_id=${chatId} \
        -d text='${message}'
    """
}
