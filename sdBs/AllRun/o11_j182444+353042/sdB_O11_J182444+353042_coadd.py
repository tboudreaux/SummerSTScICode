from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[276.183333,35.511667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J182444+353042/sdB_O11_J182444+353042_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J182444+353042/sdB_O11_J182444+353042_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
