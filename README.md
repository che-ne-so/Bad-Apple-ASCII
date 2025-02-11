<h1>ASCII Video Player</h1>

<p>A simple project to convert Bad Apple video into ASCII art and play audio in sync with the video.</p>

<h2>Requirements:</h2>
<ul>
  <li><strong>Python 3.x</strong></li>
  <li><strong>opencv-python</strong> (for image and video manipulation)</li>
  <li><strong>numpy</strong> (for handling image data)</li>
  <li><strong>playsound==1.2.2</strong> (for audio playback)</li>
  <li><strong>threading</strong> (to run audio in a separate thread)</li>
</ul>

<h2>Installation:</h2>
<p>You can install the required dependencies using the following command:</p>

<pre><code>pip install opencv-python numpy playsound==1.2.2</code></pre>

<p><em>Tip:</em> Make sure you have a good PC to run this project smoothly.</p>
<p><em>Tip 2:</em> Is recommended to open the CMD window in fullscreen for a better view.</p>

<h2>How It Works:</h2>

<h3>Image to ASCII Conversion:</h3>
<ul>
  <li>The function <code>image_to_ascii()</code> converts each video frame into an ASCII representation.</li>
  <li>Frames are resized to fit the terminal width, maintaining the original aspect ratio of the video.</li>
</ul>
<p><em>Tip:</em> To adjust the ASCII resolution, change the value of the <code>new_width</code> variable (default: <strong>100</strong>).</p>

<h3>Video Playback:</h3>
<ul>
  <li>The <code>play_video_ascii()</code> function captures video frames using OpenCV.</li>
  <li>The frames are then converted to grayscale and translated into ASCII art, which is output to the console.</li>
</ul>

<h3>Audio Playback:</h3>
<ul>
  <li>The audio is played in sync with the video using the <strong>playsound</strong> library.</li>
  <li>Audio runs in a separate thread to ensure proper synchronization.</li>
  <li>The audio is extracted from the video and stored as an MP3 file for playback.</li>
</ul>

<h2>How to Run the Project:</h2>
<ol>
  <li>Extract the project</li>
  <li>Navigate to the project directory:</li>
  <p>e.g.</p>
  <pre><code>cd C:\Users\user\Downloads\Bad-Apple-ASCII-main</code></pre>

  <li>Run the Python script using this command:</li>
  <pre><code>python bad_apple.py</code></pre>

  <li>Done</li>

<h2>Notes:</h2>
<ul>
  <li>The script clears the console screen between frames to properly display the ASCII animation.</li>
  <li>Active waiting is used to ensure the frames are displayed at the correct speed based on the video's frames per second (FPS).</li>
</ul>
