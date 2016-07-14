from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.924875,-59.943056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ngc6752_3675/sdB_ngc6752_3675_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ngc6752_3675/sdB_ngc6752_3675_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
