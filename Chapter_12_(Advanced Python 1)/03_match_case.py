# Here, we are matching the 'status'
def http_status(status):
    match status:
        case 200:  # if status is 200
            return "ok"
        case 404:  # if status is 400
            return "Not Found"
        case 500:  # if status is 500
            return "Internal Server Error"
        case _:  # default case
            return "Unknown Status"  # if none of the case matches, do this


print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(403))
