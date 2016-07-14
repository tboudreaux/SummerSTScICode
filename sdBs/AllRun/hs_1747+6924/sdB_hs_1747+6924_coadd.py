from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[266.770167,69.388217],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_1747+6924/sdB_hs_1747+6924_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_1747+6924/sdB_hs_1747+6924_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
