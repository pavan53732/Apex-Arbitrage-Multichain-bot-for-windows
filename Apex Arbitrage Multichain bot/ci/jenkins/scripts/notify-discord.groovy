def call(String message, String webhookUrl) {
    sh """
        curl -X POST -H 'Content-Type: application/json' \
        -d '{"content":"${message}"}' \
        ${webhookUrl}
    """
}
