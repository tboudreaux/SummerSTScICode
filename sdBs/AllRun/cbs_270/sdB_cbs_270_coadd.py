from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.478375,48.809969],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cbs_270/sdB_cbs_270_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cbs_270/sdB_cbs_270_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
