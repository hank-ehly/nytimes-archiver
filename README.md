# nytimes-archiver

Demonstrates how to pull data from the New York Times archive API and insert it into a mysql database.

### Setup

##### 1. Install pip packages
```bash
pip install requirements
```

##### 2. Create mysql db
```mysql
CREATE DATABASE IF NOT EXISTS [db] DEFAULT CHARACTER SET UTF8MB4;
GRANT ALL PRIVILEGES ON [db].* TO [user]@[host] IDENTIFIED BY [password];
```

##### 3. Add your local settings
```bash
cp settings.py settings.py.example 
# Now add your API key to settings.py
```

##### 4. Run
```bash
python archive.py
```

### License

The MIT License (MIT)

Copyright (c) 2018 Hank Ehly

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
