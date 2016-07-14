from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[189.771458,48.439806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_123905.15+482623.3/sdB_SDSSJ_123905.15+482623.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_123905.15+482623.3/sdB_SDSSJ_123905.15+482623.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
