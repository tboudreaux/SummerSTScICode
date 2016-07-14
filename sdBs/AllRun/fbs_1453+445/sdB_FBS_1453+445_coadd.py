from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[223.905,44.309194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_1453+445/sdB_FBS_1453+445_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_1453+445/sdB_FBS_1453+445_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
