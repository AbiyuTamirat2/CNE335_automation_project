# This is the template code for the CNE335 Final Project
# Abiyu Gebremeskel
# CNE 335 Winter
# Reference: https://rtc.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=8d8f14d6-adc0-4918-9e18-b12b0033c7cd&autoplay=False&interactivity=all&start=0&showtitle=True&offerviewer=True&captions=False&showbrand=True&ltiCourseID=Canvas%5c2439011&isLTIEmbed=true&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyIsImtpZCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyJ9.eyJpc3MiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIiLCJhdWQiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIvcmVzb3VyY2VzIiwiZXhwIjoxNzEwMjk4NDU4LCJuYmYiOjE3MTAyOTgzOTgsImNsaWVudF9pZCI6ImMzMTNkZWEzLWIyZjgtNDFlNi05NDQwLWFkNDEwMDYzYTY3YSIsInNjb3BlIjoidmlld0VtYmVkZGVkQ29udGVudCIsInN1YiI6ImIyMWQwNzI5LWRkMzAtNDJmYi04NmU1LWFlOTgwMTRlODUzMCIsImF1dGhfdGltZSI6MTcxMDI5ODM5OCwiaWRwIjoiaWRzcnYiLCJyb2xlIjoidmlld2VyIiwic2Vzc2lvbl9pZCI6ImY4YmUzOWY0LTk2NTYtNGQ3OC05MjdkLWIxMzIwMDJmOTljOSIsIm5hbWUiOiJBYml5dSBHZWJyZW1lc2tlbCIsImFtciI6WyJwYXNzd29yZCJdfQ.H5omOQ6-s0JYPtRN-V7E4dZ70RBCah7_4WG_R0XsxG21B01ybmM1DBiR6ZXp7K2akogLTPhT2uPBRBK2ET_07YPMRtNILWWSqarJbOWT47sXJCuA8LSV9wFapDGdFyhhES-MBDKcr2EubYxJMQI5er4qDEKSu6mmInPKtiiFE3-wy9wlMGwTb6s04GgIm_5mzyoGOooxP2p_uzoWwZXuH-Jtz6qTPKUM6I7DBIWMbfky9gUeO_qkD4R_JtABs3rY9X1fj7Svh1v2O2gDUP1S0BohP7LEAy4j1mK8MIOOQQIe5C5m9nFweeawNeoitGxm0ZooZQZ26xcr7trwpu-LwQ#access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyIsImtpZCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyJ9.eyJpc3MiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIiLCJhdWQiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIvcmVzb3VyY2VzIiwiZXhwIjoxNzEwMzAxOTk4LCJuYmYiOjE3MTAyOTgzOTgsImNsaWVudF9pZCI6ImMzMTNkZWEzLWIyZjgtNDFlNi05NDQwLWFkNDEwMDYzYTY3YSIsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidmlld0VtYmVkZGVkQ29udGVudCJdLCJzdWIiOiJiMjFkMDcyOS1kZDMwLTQyZmItODZlNS1hZTk4MDE0ZTg1MzAiLCJhdXRoX3RpbWUiOjE3MTAyOTgzOTgsImlkcCI6Imlkc3J2Iiwicm9sZSI6InZpZXdlciIsInNlc3Npb25faWQiOiJmOGJlMzlmNC05NjU2LTRkNzgtOTI3ZC1iMTMyMDAyZjk5YzkiLCJuYW1lIjoiQWJpeXUgR2VicmVtZXNrZWwiLCJhbXIiOlsicGFzc3dvcmQiXX0.rPoAvbexNTs50ua83rG0Qw6_CE8vjS0fn5B-FHEUwEB9TciL6ltHv4l6vhzlCkyz-RM4IZHwUuLriIJjovLar3eZdElW-YLUWeUeU8Pux_uZNjo11Kpf90HqKn5KHwhQsxXKfqV-_CiD9PV0nq3oINQGMUpv4ZeVOIV4bvSC72HQkBmU01y_pZcDrN_2dmvoqeglWWonXIKnvbGTYb7u-Ouv4b2sSVu4Bk9sMrGY5Wu4A1KNpCGRvZpal_nsJsEqHUrJWZF-3Ecro9jEuS_r1TzamB53TPFnuAuCyxCD784H3KEqc7wWrCFosmq7J8Eg-clt6Vn3mBYC0o466W1GVw


import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Abiyu")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_server = Server.Server("52.26.153.219")
    # TODO - Call Ping method and print the results
    if my_server.ping():
        print("Ping results success")
