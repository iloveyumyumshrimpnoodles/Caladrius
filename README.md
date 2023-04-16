# Caladrius
A snow-white bird that lives in the king's house

# Info
XOR encrypted, Zlib compressed, Base64 encoded Python 3 code loader

# Usage
1.Create payload:
```
python3 builder.py [scriptname]
```

2. Update the configuration in `loader.py`
    - Change `__KEY__` to the used encryption key (check terminal)
    - Change `__PAYLOAD__` to the final payload (check terminal or see "out.caladrius.py")

# How
Caladrius abuses the Python `pickle` library, and the `__reduce__` function. <br>
If `pickle.loads()` gets called on a serialized class which has the `__reduce__` function set, arbitary code can be executed (more info [here](https://davidhamann.de/2020/04/05/exploiting-python-pickle/)) <br>
This tool abuses that by making it `exec()` our custom code.

# Notes
Caladrius isn't made to load malware that runs for a long time or infinitely. It's better to use stagers that will eventually start a process that would start the actual malware. <br>
This is because I couldn't figure out how to create a orphan (no parent process) process that would run idependently from the main process. <br><br>
This was mostly made past 00.00, so excuse me if the code seems weird or funky, as my brain only works at .2% capacity :p

# Disclaimer
```
THIS PROGRAM IS DESIGNED TO BE USED FOR ETHICAL PENTESTING OR EDUCATIONAL PURPOSES ONLY. THE DEVELOPER OF THIS PROGRAM DOES NOT CONDONE OR SUPPORT ANY MALICIOUS OR ILLEGAL ACTIVITIES THAT MAY BE PERFORMED USING THIS PROGRAM. IT IS THE RESPONSIBILITY OF THE USER TO ENSURE THAT THEIR USE OF THIS PROGRAM COMPLIES WITH ALL APPLICABLE LAWS AND REGULATIONS. THE DEVELOPER OF THIS PROGRAM IS NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THE USE OF THIS PROGRAM.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE, DAMMIT.
```

# License
```
This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
```