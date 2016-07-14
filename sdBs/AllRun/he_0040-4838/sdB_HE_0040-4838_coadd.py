from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.6295,-48.371167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_0040-4838/sdB_HE_0040-4838_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_0040-4838/sdB_HE_0040-4838_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
