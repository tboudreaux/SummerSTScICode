from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.501042,-34.465247],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0231-3441/sdB_he_0231-3441_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0231-3441/sdB_he_0231-3441_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
