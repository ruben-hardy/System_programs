# Importing modules needed for analysis, pdf reader, html reader, ftp functions
import os
import sys
import nltk
import ftplib
import html2text
from nltk.tokenize import RegexpTokenizer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


class wFrequency():
    """
    Module to normalize give data and count frequency of the supplied patterns or a word.
    """
    def __init__(self, doc, pat, action, path, master_list, job_type):
        self.job_type = job_type
        self.master = master_list
        self.path = path
        self.doc = doc
        self.tmp_doc = "/ci/data/autotest/tmp{0}".format(self.doc)
        self.pat = pat
        self.action = action
        self.pstem = nltk.PorterStemmer()
        self.freq = nltk.FreqDist
        self.frequency = []
        self.bool = []
        self.log = []
        self.file_full_list = []
        self.npats = len(self.pat)
        self.filename, self.file_extension = os.path.splitext(self.doc)
        try:
            if self.file_extension == '.txt' or self.file_extension == '.log':
                txt = self.parse_txt()
                token = self.text2token(txt)
                clean_tokens = self.remove_stopwords(token)
                ngram = self.word_ngram(clean_tokens, 1, 25)
                self.frequency, self.bool, self.log, self.file_full_list = self.ngram_count(ngram)
            elif self.file_extension == '.pdf':
                pdf = self.parse_pdf()
                tokens = self.text2token(pdf)
                clean_tokens = self.remove_stopwords(tokens)
                ngram = self.word_ngram(clean_tokens, 1, 25)
                self.frequency, self.bool, self.log, self.file_full_list = self.ngram_count(ngram)

            elif self.file_extension == '.html':
                html = self.parse_html()
                tokens = self.text2token(html)
                clean_tokens = self.remove_stopwords(tokens)
                ngram = self.word_ngram(clean_tokens, 1, 25)
                self.frequency, self.bool, self.log, self.file_full_list = self.ngram_count(ngram)
            else:
                sys.stderr.write('unsupported file format %s' % self.file_extension)
        except IOError, e:
            sys.stderr.write('Errno:', e[0], '\nMessage:', e[1])


    def parse_txt(self):
        """
        Recevies .txt or .log file as argument and parse its content to text object.
        :param:
        :return: strings
        """
        if self.path[0] == 'ftp':
            self.ftp_parse()
            txt = open(self.tmp_doc.encode('utf-8')).read()
        else:
            with open(self.doc.encode('utf-8'), 'r') as handle:
                txt = handle.read()
        #self.clean()
        return txt

    def parse_pdf(self):
        """
        Receives .pdf files as argument and parse its content to a text file.
        returns text object
        :param doc:
        :return: strings
        """
        pagenos = set()
        maxpages = 0
        password = ''
        rotation = 0
        outfp = file('pdf.txt', 'w')
        rsrcmgr = PDFResourceManager(caching=True)
        device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=LAParams(), imagewriter=None)
        fp = file(self.doc, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=True,
                                      check_extractable=True):
            page.rotate = (page.rotate + rotation) % 360
            interpreter.process_page(page)
        fp.close()
        device.close()
        outfp.close()
        with open('pdf.txt', 'r') as handle:
            pdf = handle.read()
        #`()
        return pdf

    def parse_html(self):
        """
        parse html file and returns text from html as string object.
        :return:
        """
        obj = open(self.doc.encode('utf-8')).read()
        html = obj.decode('utf-8')
        parser = html2text.HTML2Text()
        parser.wrap_links = False
        parser.skip_internal_links = True
        parser.inline_links = True
        parser.ignore_anchors = True
        parser.ignore_images = True
        parser.ignore_emphasis = True
        parser.ignore_links = True
        text = parser.handle(html)
        text = text.strip(' \t\n\r')
        text = text.encode('utf-8')
        open('html.txt', 'w').write(text)
        with open('html.txt', 'r') as handle:
            html = handle.read()
        #self.clean()
        return html

    def text2token(self, txt_obj):
        """
        converts supplied strings in to tokens.
        :param txt_obj:
        :return: list
        """
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(txt_obj)
        return tokens

    def remove_stopwords(self, tokens):
        """
        converts the tokens in to lower cases. Any stopword can be included as desired in this module as enhancement.
        :param tokens:
        :return: list
        """
        clean_tokens = [w.lower() for w in tokens]
        return clean_tokens

    def word_ngram(self, tokens, min=1, max=4):
        """
        creating n-grams from the supplied tokens
        :return:
        """
        ngrams = []
        for n in range(min, max):
            for ngram in nltk.ngrams(tokens, n):
                ngrams.append(' '.join(i for i in ngram))
        return ngrams

    def ngram_count(self, ngrams):
        """
        search for the supplied string and return it's frequency in ngram.
        '*' in pattern will be considered for the wild card matching.
        :param usr_input:
        :return: lists
        """
        hit_count = []
        file_list = []
        file_full_list = []
        hit_bool = []
        fd = self.freq(ngrams)
        for count, index in enumerate(range(len(self.pat))):
            tokenizer = RegexpTokenizer(r'[\w+^*]+')
            pat_token = tokenizer.tokenize(self.pat[index])
            pat_sent = " ".join(pat_token)
            if '*' in pat_sent:
                import fnmatch
                filtr = fnmatch.filter(ngrams, pat_sent.lower())
                refine = [x for x in filtr if len(self.pat[index].split(" ")) == len(x.split(" "))]
                if refine:
                    self.pat[count] = u'\n'.join(refine)
                    hit_count.append(len(refine))
                    hit_bool.append('True')
                else:
                    hit_count.append(0)
                    hit_bool.append('False')
            else:
                hit_count.append(fd[pat_sent.lower()])
                if fd[pat_sent.lower()] != 0:
                    hit_bool.append('True')
                else:
                    hit_bool.append('False')
                    pass
            if self.job_type == 'job' or 'auto':
                lst = (os.path.split(self.doc)[0]).split('/')
                if self.job_type == 'job':
                    del lst[0:5]
                else:
                    del lst[0:7]
                new_path = "/".join(lst)
                file_list.append(os.path.join(new_path, os.path.basename(self.doc)))
                file_full_list.append(self.doc)
            else:
                file_list.append(self.doc)
        return hit_count, hit_bool, file_list, file_full_list

    def clean(self):
        """
        clear temporary files generated during execution.
        :return: None
        """
        os.popen('rm -rf pdf.txt')
        os.popen('rm -rf html.txt')
        os.popen('rm -rf /ci/data/autotest/tmp/srv')

    def result_list(self):
        """
        Creates master list with all the result items (logs, filename, hit counts etc.)
        :return: Master list
        """
        bool, freq, pat, act, log, full_list = ([] for i in range(6))
        for index, item in enumerate(self.bool):
            bool.append(self.bool[index])
            freq.append(self.frequency[index])
            pat.append(self.pat[index])
            act.append(self.action[index])
            log.append(self.log[index])
            full_list.append(self.file_full_list[index])
        if not self.master:
            self.master = [bool, freq, pat, act, log, full_list]
        else:
            self.master = [self.master[0] + bool, self.master[1] + freq, self.master[2] + pat, self.master[3] + act, self.master[4] + log, self.master[5] + full_list]
        return self.master

    def ftp_parse(self):
        """
        creates a local copy of the FTP file for text analysis
        :return: None
        """
        os.makedirs(os.path.split(self.tmp_doc)[0])
        try:
            ftp_client = ftplib.FTP(self.path[1], self.path[2], self.path[3])
            ftp_client.retrbinary('RETR {0}'.format(self.doc), open(self.tmp_doc, 'wb').write)
            ftp_client.quit()
        except ftplib.all_errors, e:
            sys.stderr.write('FTP ERROR(s): ', e)
