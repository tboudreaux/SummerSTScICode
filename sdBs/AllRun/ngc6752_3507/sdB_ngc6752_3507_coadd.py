from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.597167,-59.874497],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ngc6752_3507/sdB_ngc6752_3507_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ngc6752_3507/sdB_ngc6752_3507_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
