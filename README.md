# Dmusic

**Tác giả: LMD**

A FOSS YouTube Music client for Android and Desktop with many features from Spotify, SponsorBlock, ReturnYouTubeDislike using Compose Multiplatform to develop.

## Features ✨️
- Play music from YouTube Music or YouTube for free, without ads and in the background
- Recognize the song playing near you, then find it in Dmusic (Android) (NEW)
- Add your own synced lyrics, line by line or word by word, to songs that have none (NEW)
- Read YouTube comments in Now Playing, and post, reply or like them when signed in (NEW)
- Your library sidebar on Desktop with your playlists, albums, artists and podcasts (NEW)
- Three Now Playing styles: Classic, Material 3 Expressive and a redesigned Apple Music player with Apple Music-style lyrics (NEW)
- Ten-band equalizer with presets and AutoEq headphone profiles, plus Delay and Reverb effects, or your phone's system equalizer on Android (NEW)
- Pick the speaker, headphones or Cast device Dmusic plays on, without moving other apps' audio (NEW)
- Dmusic Wrapped: your year in music, plus monthly recap playlists (NEW)
- On-device listening analytics: charts, period history, listening clock and a shareable listening receipt (NEW)
- Word-by-word Apple Music-style lyrics, romanization for 12 languages, share lyrics as an image, landscape fullscreen lyrics and a timing offset (NEW)
- Home screen widgets: turntable, playlists and listening insights (NEW)
- Send your sign-ins from Android to Desktop by scanning a QR code (NEW)
- Preferred audio language for videos with several audio tracks (NEW)
- High quality up-to 256kbps stream (Opus or AAC) for YouTube Music Premium users
- Browsing Home, Charts, Podcast, Moods & Genre with YouTube Music data at high speed
- Search everything on YouTube
- Spotify Canvas and Animated Album Art supported (NEW)
- Power your experience with Dmusic Chart
- Play 1080p video option with subtitle
- Play YouTube Music live stations (NEW)
- AI song suggestions and an AI reading of your music taste (NEW)
- Import playlists converted from Spotify and other apps
- Customize your playlist, synced with YouTube Music
- Notifications from followed artists
- Caching and offline playback support, plus Smart downloads of the songs you play most (Android) (NEW)
- Crossfade with DJ-style like Apple Music
- Customizing THEME (Light, Dark, Color, etc)
- Synced lyrics from Dmusic Lyrics, LRCLIB, BetterLyrics, Spotify (require login) and YouTube Transcript - AI lyrics translation (BETA) (*)
- Personalize data (**) and multi-YouTube-account support
- Dislike songs on YouTube Music so it recommends them less (NEW)
- Last.fm scrobbling (Full version)
- Supports SponsorBlock and Return YouTube Dislike
- Sleep Timer
- Android Auto with online content, feature rich UI/UX
- Discord Rich Presence support
- Listen Together: shared rooms that play in sync with friends, compatible with Metrolist (NEW)
- And many more!

> (*) Use your OpenAI or Gemini API key  
> (**) For users who chose "Send back to Google" feature  

> **Warning**  
> This app is in the beta stage, so it may have many bugs and make it crash. If you find any bugs, please create an issue or contact via email: ledanh2k16@gmail.com.  
> Because of depending on YouTube Music, player errors may happen normally, please keep that in mind regarding the app's stability.

## Screenshots
<p align="center">
  <img src="asset/screenshot/01.png" width="200" />
  <img src="asset/screenshot/02.png" width="200" />
  <img src="asset/screenshot/03.png" width="200" />
  <img src="asset/screenshot/04.png" width="200" />
</p>
<p align="center">
  <img src="asset/screenshot/05.png" width="200" />
  <img src="asset/screenshot/06.png" width="200" />
  <img src="asset/screenshot/07.png" width="200" />
  <img src="asset/screenshot/08.png" width="200" />
</p>
<p align="center">
  <img src="asset/screenshot/09.png" width="200" />
  <img src="asset/screenshot/10.png" width="200" />
  <img src="asset/screenshot/11.png" width="200" />
  <img src="asset/screenshot/12.png" width="200" />
</p>
<p align="center">
  <img src="asset/screenshot/13.png" width="200" />
  <img src="asset/screenshot/14.png" width="200" />
  <img src="asset/screenshot/15.png" width="200" />
  <img src="asset/screenshot/16.png" width="200" />
</p>
<p align="center">
  <img src="asset/screenshot/17.png" width="200" />
  <img src="asset/screenshot/18.png" width="200" />
</p>
<p align="center">
  <img src="asset/screenshot/19.png" width="800" />
</p>

## Data
- This app uses hidden API from YouTube Music with some tricks to get data from YouTube Music.
- Use Spotify Web API and some tricks to get Spotify Canvas and Lyrics.
- Thanks to [InnerTune](https://github.com/z-huang/InnerTune/) for the idea to get data from YouTube Music.
- Special thanks to [SmartTube](https://github.com/yuliskov/SmartTube) for helping extract the streaming URL of YouTube Music.
- My app is using [SponsorBlock](https://sponsor.ajay.app/) to skip sponsor in YouTube videos.
- ReturnYouTubeDislike for getting information on votes.
- Main lyrics data from Dmusic Lyrics.
- Alternative lyrics data from LRCLIB. More information [LRCLIB](https://lrclib.net/).
- Song recognition by Shazam, with the recognizer ported from Metrolist.

## Privacy
Dmusic doesn't have any tracker or third-party server for collecting user data in FOSS version. If YouTube logged-in users enable "Send back to Google" feature, Dmusic only uses YouTube Music Tracking API to send listening history and listening record of video to Google for better recommendations and supporting artist or YouTube Creator.

We collect crash data in the Full version to improve the app.

## Full or FOSS version
Crashlytics is used to catch crashes in the Full version to help improve stability. If you do not want crash data to be collected, you can use the FOSS version.

## Desktop app

### Which file should I download?
- For Windows: Download `Dmusic-Windows-installer.zip`, unzip it and run `install.bat`.
- For macOS (macOS 15 or newer): Download the file with extension `.dmg`.
- For Linux: Download the file with extension `.AppImage` (all Linux distributions).

### Some limitations on Desktop app:
- Some Linux distributions may have stability issues (upstream JetBrains issue).
- ARM64 on Windows and Linux: use the x64 build.

Please report issues on GitHub if you find any bugs.

## FAQ
#### 1. Wrong Lyrics?
Lyrics are provided by LRCLIB and other sources. Sometimes lyrics may not match perfectly with the YouTube `videoId` parameter. So we need to use some "String Matcher" and "Duration" to search lyrics. So sometimes, some songs or videos get the wrong lyrics.

#### 2. Why the name "Dmusic"?
Dmusic is designed to provide you with everything you need for a powerful, seamless music streaming experience.

## Contributing
Dmusic is exclusively developed and maintained by LMD. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Legal Disclaimer & Terms of Use

### 1. 100% Free, Open-Source & Strictly Non-Commercial
Dmusic is a fully open-source project (FOSS) created purely for educational purposes and personal use. **We do not sell this application, nor do we monetize it in any way.** There are no advertisements, no premium features, no subscriptions, and no hidden fees within the app. This project has absolutely no commercial value or financial intent.

### 2. A Custom Browser with Content Filtering
Dmusic acts strictly as a specialized, third-party web browser and client. It simply parses the publicly available website content and APIs of YouTube and YouTube Music, rendering them in a custom user interface. The ad-free experience it provides is fundamentally no different from using a standard web browser (like Chrome, Firefox, or Brave) equipped with a common ad-blocking extension (such as uBlock Origin).

### 3. Support Content Creators
We deeply respect the hard work of artists, musicians, and content creators. **We strongly encourage all users to subscribe to [YouTube Premium](https://www.youtube.com/premium).** Purchasing a Premium subscription is the best way to financially support the creators you listen to and ensure the continued growth of the platform. Dmusic is built as a proof-of-concept for developers and enthusiasts, not to harm creators' revenues.

### 4. No Hosting of Copyrighted Material
We do not host, upload, distribute, or store any audio, video, or copyrighted media files on our own servers. All content accessed through this application is stored entirely on Google's/YouTube's servers and remains the property of their respective copyright owners. The app merely acts as a conduit to stream publicly accessible links.

### 5. User Responsibility & Legal Contact
The software is provided "AS IS", without warranty of any kind. The developer (LMD) of Dmusic does not encourage or condone piracy. Users are solely responsible for ensuring their usage of this app complies with their local copyright laws and the Terms of Service of the platforms they access.

Because we do not host any media files, we cannot process DMCA takedown requests for audio or video content. However, if you represent a copyright holder or have legal concerns regarding the open-source code itself, please contact us via email at: **ledanh2k16@gmail.com**
