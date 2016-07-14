from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[32.881292,39.287139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0208+390/sdB_FBS_0208+390_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0208+390/sdB_FBS_0208+390_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
