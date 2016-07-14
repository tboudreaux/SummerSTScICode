from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[57.130417,0.771319],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_03459+0037/sdB_kuv_03459+0037_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_03459+0037/sdB_kuv_03459+0037_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
