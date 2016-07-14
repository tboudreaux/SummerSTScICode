from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[238.135792,20.454031],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_15503+2036/sdB_kuv_15503+2036_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_15503+2036/sdB_kuv_15503+2036_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
