from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.347417,22.80625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_165323.38+224822.5/sdB_SDSSJ910_165323.38+224822.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_165323.38+224822.5/sdB_SDSSJ910_165323.38+224822.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
