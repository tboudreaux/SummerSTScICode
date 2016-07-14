from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.73025,28.143839],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_12485+2825/sdB_kuv_12485+2825_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_12485+2825/sdB_kuv_12485+2825_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()