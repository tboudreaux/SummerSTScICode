from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[298.909208,-23.228228],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lse_21/sdB_lse_21_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lse_21/sdB_lse_21_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
