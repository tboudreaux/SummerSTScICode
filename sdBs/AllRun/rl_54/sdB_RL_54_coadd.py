from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[94.678417,21.59315],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_RL_54/sdB_RL_54_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_RL_54/sdB_RL_54_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
