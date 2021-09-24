use std::io::{Read, Result, Write};

pub struct ReadStats<R> {
    reader: R,
    nreads: usize,
    nbytes: usize,
}

impl<R: Read> ReadStats<R> {
    // _wrapped is ignored because R is not bounded on Debug or Display and therefore
    // can't be passed through format!(). For actual implementation you will likely
    // wish to remove the leading underscore so the variable is not ignored.
    pub fn new(_wrapped: R) -> ReadStats<R> {
        Self {
            reader: _wrapped,
            nreads: 0,
            nbytes: 0,
        }
    }

    pub fn get_ref(&self) -> &R {
        &self.reader
    }

    pub fn bytes_through(&self) -> usize {
        self.nbytes
    }

    pub fn reads(&self) -> usize {
        self.nreads
    }
}

impl<R: Read> Read for ReadStats<R> {
    fn read(&mut self, buf: &mut [u8]) -> Result<usize> {
        let nbytes = self.reader.read(buf)?;
        self.nbytes += nbytes;
        self.nreads += 1;

        Ok(nbytes)
    }
}

pub struct WriteStats<W> {
    writer: W,
    nwrites: usize,
    nbytes: usize,
}

impl<W: Write> WriteStats<W> {
    // _wrapped is ignored because W is not bounded on Debug or Display and therefore
    // can't be passed through format!(). For actual implementation you will likely
    // wish to remove the leading underscore so the variable is not ignored.
    pub fn new(_wrapped: W) -> WriteStats<W> {
        Self {
            writer: _wrapped,
            nwrites: 0,
            nbytes: 0,
        }
    }

    pub fn get_ref(&self) -> &W {
        &self.writer
    }

    pub fn bytes_through(&self) -> usize {
        self.nbytes
    }

    pub fn writes(&self) -> usize {
        self.nwrites
    }
}

impl<W: Write> Write for WriteStats<W> {
    fn write(&mut self, buf: &[u8]) -> Result<usize> {
        let nbytes = self.writer.write(buf)?;
        self.nbytes += nbytes;
        self.nwrites += 1;

        Ok(nbytes)
    }

    fn flush(&mut self) -> Result<()> {
        self.writer.flush()
    }
}
