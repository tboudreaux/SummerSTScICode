from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.343,33.747778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_164122.32+334452.0/sdB_sdssj_164122.32+334452.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_164122.32+334452.0/sdB_sdssj_164122.32+334452.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
