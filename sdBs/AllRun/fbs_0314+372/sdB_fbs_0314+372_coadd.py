from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[49.405958,37.486944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0314+372/sdB_fbs_0314+372_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0314+372/sdB_fbs_0314+372_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
