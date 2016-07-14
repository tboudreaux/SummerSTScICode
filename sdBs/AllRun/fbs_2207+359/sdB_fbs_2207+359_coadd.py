from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[332.4335,36.163667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2207+359/sdB_fbs_2207+359_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2207+359/sdB_fbs_2207+359_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
