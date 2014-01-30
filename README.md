msf
===========

Python classes and modules for Metasploit integration

-------------------------------------------------------------------------------

Matthew C. Jones, CPA, CISA, OSCP

IS Audits and Consulting, LLC - <http://www.isaudits.net/>

TJS Deemer Dana - <http://www.tjsdd.com>

-------------------------------------------------------------------------------

This is a work in process to simplify and expedite execution of Metasploit
commands from Python when it is unnecessary for more complex functionality such
as MSFRPC. Currently consists of:

-a parent class to handle executing metasploit commands 
-subclasses for direct interaction in your code

Current functionality is limited to parsing and executing an msfconsole command
using the msfconsole_command class:

Commands are built and piped via console similar to a resource file so multiple
handlers and exploits can be executed in a single thread
    
The "command" attribute should be a string with individual commands separated by
a semicolon; parse_msfconsole_args builds this string from individual command 
strings passed as args

Example usage is included in the "examples" folder

-------------------------------------------------------------------------------

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
this program. If not, see <http://www.gnu.org/licenses/>.
