from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[235.962417,33.90125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_154350.98+335404.5/sdB_SDSSJ910_154350.98+335404.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_154350.98+335404.5/sdB_SDSSJ910_154350.98+335404.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
