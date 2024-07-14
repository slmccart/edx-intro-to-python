import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Looking for src="http://www.youtube.com/embed/xvFZjo5PgG0" within <iframe ...></iframe> in HTML input
    if html_matches := re.search(r"^<iframe .*src=\"(\S+)\" ?.*></iframe>$", s):
        link = html_matches.group(1)
        # Given a Youtube link like http://www.youtube.com/embed/xvFZjo5PgG0, shorten the url to something like https://youtu.be/xvFZjo5PgG0
        if youtube_matches := re.search(r"^(?:https?://)?(?:www.)?youtube.com/embed/(.+)$", link):
            video_id = youtube_matches.group(1)
            return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()
