from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[214.587167,-3.381692],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_1415-0309/sdB_HE_1415-0309_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_1415-0309/sdB_HE_1415-0309_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
