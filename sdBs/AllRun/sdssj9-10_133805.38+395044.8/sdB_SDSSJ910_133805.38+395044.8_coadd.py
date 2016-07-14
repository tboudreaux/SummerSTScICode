from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[204.522417,39.845778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_133805.38+395044.8/sdB_SDSSJ910_133805.38+395044.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_133805.38+395044.8/sdB_SDSSJ910_133805.38+395044.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
