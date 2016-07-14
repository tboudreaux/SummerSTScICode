from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[286.145833,48.172778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j190435+481022/sdB_o11_j190435+481022_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j190435+481022/sdB_o11_j190435+481022_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
