PRODUCT_NAME := M3K.fw
TOPDIR := $(shell pwd)/
OUTDIR := $(TOPDIR)/recovery-update
IMAGE_SRC ?= $(TOPDIR)/image
RES_SRC := $(TOPDIR)/../resource
SECURITY := $(RES_SRC)/security
KEYNAME := testkey
SOURCE := pack.sh

all: $(SOURCE)
	@./$(SOURCE) $(OUTDIR) $(IMAGE_SRC) $(SECURITY) $(KEYNAME)
	zip -r $(PRODUCT_NAME) recovery-update

clean:
	@rm -rf $(OUTDIR)
