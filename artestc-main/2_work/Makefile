all:
	$(MAKE) -C libmysyslog
	$(MAKE) -C libmysyslog-text
	$(MAKE) -C libmysyslog-json
	$(MAKE) -C libmysyslog-client
	$(MAKE) -C libmysyslog-daemon

clean:
	$(MAKE) -C libmysyslog clean
	$(MAKE) -C libmysyslog-text clean
	$(MAKE) -C libmysyslog-json clean
	$(MAKE) -C libmysyslog-client clean
	$(MAKE) -C libmysyslog-daemon clean

install:
	$(MAKE) -C libmysyslog install
	$(MAKE) -C libmysyslog-text install
	$(MAKE) -C libmysyslog-json install
	$(MAKE) -C libmysyslog-client install
	$(MAKE) -C libmysyslog-daemon install
