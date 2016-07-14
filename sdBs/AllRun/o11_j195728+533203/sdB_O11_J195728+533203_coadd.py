from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[299.366667,53.534167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J195728+533203/sdB_O11_J195728+533203_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J195728+533203/sdB_O11_J195728+533203_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
